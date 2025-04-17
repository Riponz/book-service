import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Card from '../Components/Card'
import { useNavigate } from 'react-router-dom'
import Cookies from "js-cookie"
import { toast } from 'react-toastify'
import { useUser } from '../Components/Context';
import { jwtDecode } from 'jwt-decode';


function Home() {

    // const token = Cookies.get('token');
    // const loggedIn = token && isTokenValid(token);


    const { user, setUser } = useUser();
    const navigate = useNavigate()
    const [books, setBooks] = useState()
    const token = Cookies.get('token')
    const notify = (msg) => toast(msg);
    const GET_USER_API = "http://127.0.0.1:5000/users/me/"

    const BOOK_URL = "http://127.0.0.1:8000/api/v1/books/"

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

        const fetch_books = async () => {
            await axios.get(BOOK_URL)
                .then(data => {
                    setBooks(data?.data?.data)
                }).catch(err => {
                    notify(err?.response.data.error)
                })
        }

        fetch_books()

    }, [])

    useEffect(() => {
        const getUser = async () => {
            await axios.get(GET_USER_API, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }).then(data => {
                setUser(data?.data)
                Cookies.set('id', data?.data.id)
            }).catch(err => {
                notify("Error geting user")
            })
        }

        getUser()

    }, [])



    return (
        <div className='w-full h-full flex flex-col justify-start items-center gap-3'>
            {
                books?.map(book => (
                    <Card key={book.id} id={book.id}
                        title={book.title}
                        author={book.author}
                        genre={book.genre} />
                ))
            }
        </div>
    )
}

export default Home