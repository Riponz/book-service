import axios from 'axios'
import React, { useEffect } from 'react'
import { useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import Cookies from 'js-cookie'
import { toast } from 'react-toastify';
import { useUser } from '../Components/Context';
import { jwtDecode } from 'jwt-decode'

function Detail() {

    const { user, setUser } = useUser();

    const { id } = useParams()
    const [book, setBook] = useState()
    const notify = (msg) => toast(msg);
    const token = Cookies.get('token')
    const navigate = useNavigate()


    const GET_BOOK_URL = `http://127.0.0.1:8000/api/v1/books/${id}`
    const RENT_BOOK_URL = `http://127.0.0.1:5000/api/v1/users/${user?.id}/rent/${id}`

    useEffect(() => {
            const isTokenValid = (token) => {
                try {
                    const decoded = jwtDecode(token);
                    const now = Date.now() / 1000; // in seconds
                    return decoded.exp > now;
                } catch (e) {
                    return false;
                }
            }
    
            const loggedIn = token && isTokenValid(token)
    
            if (!loggedIn) {
                notify("Token Expired. Login Again")
                navigate('/login')
            }
        }, [])


    useEffect(() => {
        const token = Cookies.get('token')

        if (!token) {
            navigate('/login')
        }
        const fecthBook = async () => {
            await axios.get(GET_BOOK_URL)
                .then(data => {
                    setBook(data?.data?.data)
                })
        }

        fecthBook()
    }, [])

    const handleRent = async () => {
        await axios.post(RENT_BOOK_URL, {}, {
            headers: {
                'Authorization': `Bearer ${Cookies.get('token')}`
            }
        }).then(data => {
            notify("Book Rented Successfully")
        }).catch(err => {
            if (err.response?.status_code === 401) {
                notify("User Not Authorized")
            } else {
                notify("Book Not available")
            }
        })
    }


    return (
        <div className='h-[75%] w-full flex justify-center items-center'>

            <div className="container bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[40%] h-[50%] flex flex-col justify-center items-center gap-4">
                <div className="details flex flex-col justify-center items-center gap-2">
                    <div className='text-6xl font-bold'>{book?.title}</div>
                    <div className="metadata text-sm"><span className='font-semibold'>By</span>: {book?.author} <span className='font-semibold'>Genre</span>: {book?.genre}</div>
                    <div className="metadata text-sm"><span className='font-semibold'>Available</span>: {book?.availability}</div>
                </div>
                <div onClick={handleRent} className={`btn py-1 px-2 cursor-pointer bg-white/30 shadow-xl bg-clip-padding backdrop-filter  backdrop-blur backdrop-saturate-100 backdrop-contrast-100 rounded-lg `}>
                    Book
                </div>
            </div>

        </div>
    )
}

export default Detail