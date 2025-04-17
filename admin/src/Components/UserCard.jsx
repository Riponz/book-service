import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { toast } from 'react-toastify'

function UserCard({ id, email, name, username}) {
    const navigate = useNavigate()

    

    const notify = (msg) => toast(msg)

    const DELETE_BOOK_URL = `https://book-service-7p3c.onrender.com/api/v1/books/${id}/delete`

    const handleBookDelete = async () => {
        await axios.delete(DELETE_BOOK_URL)
        .then(data => {
            if(data.status === 200){
                notify("Book Deleted Successfully")
                toggle(!ref)
            }
        }).catch(err => {
            console.log(err)
        })
    }

    return (
        <div className='bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[90%] border-1 border-slate-200 h-max p-4 flex justify-between items-center'>
            <div className="details">
                <div className="name text-2xl font-bold">{name}</div>
                <div className="details flex justify-start items-center gap-4">
                    <div className="author">Username: {username}</div>
                    <div className="genre">Email: {email}</div>
                </div>
            </div>
        </div>
    )
}

export default UserCard