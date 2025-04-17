import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { toast } from 'react-toastify'

function Card({ id, title, author, genre, available, ref, toggle }) {
    const navigate = useNavigate()

    

    const notify = (msg) => toast(msg)

    const DELETE_BOOK_URL = `http://127.0.0.1:8000/api/v1/books/${id}/delete`

    const handleDetails = () => {
        navigate(`/book/${id}`)
    }

    const handleBookDelete = async (e) => {
        e.stopPropagation()
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
        <div onClick={handleDetails} className='bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[90%] border-1 border-slate-200 h-max p-4 flex justify-between items-center'>
            <div className="details">
                <div className="name text-2xl font-bold">{title}</div>
                <div className="details flex justify-start items-center gap-4">
                    <div className="author">Author: {author}</div>
                    <div className="genre">Genre: {genre}</div>
                </div>
            </div>
            <div onClick={handleBookDelete} className="delete-btn cursor-pointer bg-red-400 p-2 rounded-xl hover:bg-red-500 hover:shadow-sm hover:shadow-slate-400">Delete</div>

        </div>
    )
}

export default Card