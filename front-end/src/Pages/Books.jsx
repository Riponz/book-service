import axios from 'axios'
import React, { useEffect, useState } from 'react'
import Cookies from 'js-cookie'
import RentCard from '../Components/RentCard'
import { jwtDecode } from 'jwt-decode'
import {toast} from 'react-toastify'
import { useNavigate } from 'react-router-dom'


function Books() {

    const RENT_BOOK_URL = "http://127.0.0.1:5000/api/v1/rents"
    const RENT_BOOK_DETAILS = "http://127.0.0.1:8000/api/v1/books/rents"
    const GET_USER_API = "http://127.0.0.1:5000/users/me/"
    const token = Cookies.get('token')
    const [user, setUser] = useState()
    const [rents, setRents] = useState()
    const [books, setBooks] = useState()
    const navigate = useNavigate()

    const notify = (msg) => toast(msg)




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
        const getUser = async () => {
            await axios.get(GET_USER_API, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }).then(data => {

                setUser(data?.data)
            }).catch(err => {
                notify("Error geting user")
            })
        }

        getUser()

    }, [])


    useEffect(() => {
        const fetchRents = async () => {
            await axios.get(`${RENT_BOOK_URL}/${user?.id}`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            }).then(data => {
                setRents(data?.data?.data)
            }).catch(err => {
                console.log(err)
            })
        }

        fetchRents()

    }, [user])



    useEffect(() => {
        const fetchRentedBooks = async () => {
            console.log(rents)
            await axios.post(RENT_BOOK_DETAILS, { books: rents })
                .then(data => {
                    setBooks(data?.data?.data)
                }).catch(err => {
                    console.log(err)
                })
        }

        fetchRentedBooks()

    }, [rents])

    return (
        <div className='w-full h-[75%] flex flex-col justify-start items-center gap-4'>
            {
                books?.map(book => (
                    <RentCard key={book.id} bid={book.id}
                        title={book.title}
                        author={book.author}
                        genre={book.genre}
                        available={-1} />
                ))
            }

            {
                // console.log(user)
            }

        </div>
    )
}

export default Books