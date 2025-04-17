import React, { useState } from 'react'
import axios from 'axios'
import { toast } from "react-toastify"

function AddBook() {

    const [title, setTitle] = useState()
    const [author, setAuthor] = useState()
    const [genre, setGenre] = useState()
    const [available, setAvailable] = useState()

    const notify = (msg) => toast(msg)

    const ADD_BOOK_URL = "https://book-service-7p3c.onrender.com/api/v1/books/"


    const handleTitle = (e) => {
        setTitle(e.target.value)
    }

    
    const handleAuthor = (e) => {
        setAuthor(e.target.value)
    }

    
    const handleGenre = (e) => {
        setGenre(e.target.value)
    }

    
    const handleAvailable = (e) => {
        setAvailable(e.target.value)
    }

    const handAddBook = async (e) => {
        e.preventDefault()
        await axios.post(ADD_BOOK_URL, {
            "title" : title,
            "author" : author,
            "genre" : genre,
            "availability" : available
        }).then(data => {
            console.log(data)
            if(data?.status === 201){
                notify("Book Added Successfully")
                setTitle("")
                setAuthor("")
                setGenre("")
                setAvailable("")
            }
        }).catch(err => {
            console.log(err)
        })
    }

    

    return (
        <div className='w-full h-[75%] flex justify-center items-center'>
            <form onSubmit={handAddBook} className='p-8 flex flex-col justify-center items-start gap-6 rounded-2xl bg-slate-100/30 shadow-xl bg-clip-padding backdrop-filter backdrop-blur backdrop-saturate-100 backdrop-contrast-100 border-1 border-slate-300' action="">
                <div className='w-full text-center text-2xl font-bold'>Add Book</div>
                <div className='flex justify-center items-center gap-3'>
                    <label htmlFor="title">Title:</label>
                    <input className='border-1 border-slate-300 rounded-lg p-1' onChange={handleTitle} type="text" value={title} id="title" placeholder="Enter book title" />
                </div>
                <div className='flex justify-center items-center gap-3'>
                    <label htmlFor="author">Author:</label>
                    <input className='border-1 border-slate-300 rounded-lg p-1' onChange={handleAuthor} type="text" value={author} id="author" placeholder="Enter author name" />
                </div>
                <div className='flex justify-center items-center gap-3'>
                    <label htmlFor="genre">Genre:</label>
                    <input className='border-1 border-slate-300 rounded-lg p-1' onChange={handleGenre} type="text" value={genre} id="genre" placeholder="Enter book genre" />
                </div>
                <div className='flex justify-center items-center gap-3'>
                    <label htmlFor="quantity">Quantity:</label>
                    <input className='border-1 border-slate-300 rounded-lg p-1' onChange={handleAvailable} type="number" value={available} id="quantity" placeholder="Enter quantity" />
                </div>
                <div className="btn w-full flex justify-center items-center"><button type='submit' className='bg-slate-300 rounded-lg p-2 hover:bg-slate-400 cursor-pointer'>ADD➕</button></div>
            </form>
        </div>
    )
}

export default AddBook