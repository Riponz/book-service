import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useUser } from './Context'
import axios from 'axios'
import Cookies from 'js-cookie'
import { toast } from 'react-toastify'

function RentCard({ bid, title, author, genre, available }) {

    const { user } = useUser()
    const navigate = useNavigate()
    const notify = (msg) => toast(msg)

    console.log(user)

    const RETURN_BOOK_URL = `http://127.0.0.1:5000/api/v1/users/${user?.id}/return/${bid}`

    const handleReturn = async () => {
        await axios.post(RETURN_BOOK_URL, {}, {
            headers: {
                'Authorization': `Bearer ${Cookies.get('token')}`
            }
        }).then(data => {
            if (data.status === 200) {
                notify("Book Returned Successfully")
            } else {
                notify("Error Returning Book")
            }
        }).catch(err => {
            console.log(err)
        })
    }

    return (
        <div className='bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[90%] border-1 border-slate-200 h-max p-4 flex justify-between items-center'>
            <div className="details">
                <div className="name text-2xl font-bold">{title}</div>
                <div className="details flex justify-start items-center gap-4">
                    <div className="author">Author: {author}</div>
                    <div className="genre">Genre: {genre}</div>
                </div>
            </div>

            <div onClick={handleReturn} className="delete-btn cursor-pointer bg-slate-400 p-2 rounded-xl hover:bg-slate-500 hover:shadow-sm hover:shadow-slate-400">Return</div>

        </div>
    )
}

export default RentCard