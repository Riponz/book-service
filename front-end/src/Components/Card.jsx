import React from 'react'
import { useNavigate } from 'react-router-dom'

function Card({ id, title, author, genre, available }) {
    const navigate = useNavigate()

    const handleDetail = () => {
        navigate(`/book/${id}`)
    }

    return (
        <div onClick={handleDetail} className='bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[90%] border-1 border-slate-200 h-max p-4 flex justify-between items-center'>
            <div className="details">
                <div className="name text-2xl font-bold">{title}</div>
                <div className="details flex justify-start items-center gap-4">
                    <div className="author">Author: {author}</div>
                    <div className="genre">Genre: {genre}</div>
                </div>
            </div>

        </div>
    )
}

export default Card