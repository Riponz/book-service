import axios from 'axios'
import React, { useState } from 'react'
import { toast } from 'react-toastify'

function Update({ id, update, toggle }) {
  const [title, setTitle] = useState()
  const [author, setAuthor] = useState()
  const [genre, setGenre] = useState()
  const [available, setAvailable] = useState()

  const notify = (msg) => toast(msg)

  const UPDATE_BOOK_URL = "https://book-service-7p3c.onrender.com/api/v1/books"


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


  const handleUpdate = async (e) => {
    e.preventDefault()
    const payload = {
      "title": title,
      "author": author,
      "genre": genre,
      "availability": available
    }
    await axios.put(`${UPDATE_BOOK_URL}/${id}/update`, payload)
      .then(data => {
          toggle(!update)
          notify("Book Updated Successfully")
      }).catch(err => {
        console.log(err)
      })
  }

  const handleUpdatePopDown = () => {
    toggle(!update)
  }

  return (
    <div className='w-full h-full flex z-9 justify-center absolute top-0 left-0 items-center bg-black/40'>
      <form onSubmit={handleUpdate} className='p-8 relative flex flex-col z-10 justify-center items-start gap-6 rounded-2xl bg-white shadow-xl bg-clip-padding backdrop-filter backdrop-blur backdrop-saturate-100 backdrop-contrast-100 border-1 border-slate-300' action="">

        <div onClick={handleUpdatePopDown} className='absolute cursor-pointer top-5 right-5 text-xl'>x</div>

        <div className='w-full text-center text-2xl font-bold text-black'>Update Book</div>
        <div className="w-full text-center metadata text-sm text-slate-400">fill only those you want to update</div>
        <div className='flex justify-center items-center gap-3'>
          <label htmlFor="title">Title:</label>
          <input className='border-1 border-slate-500 rounded-lg p-1' onChange={handleTitle} type="text" value={title} id="title" placeholder="Enter book title" />
        </div>
        <div className='flex justify-center items-center gap-3'>
          <label htmlFor="author">Author:</label>
          <input className='border-1 border-slate-500 rounded-lg p-1' onChange={handleAuthor} type="text" value={author} id="author" placeholder="Enter author name" />
        </div>
        <div className='flex justify-center items-center gap-3'>
          <label htmlFor="genre">Genre:</label>
          <input className='border-1 border-slate-500 rounded-lg p-1' onChange={handleGenre} type="text" value={genre} id="genre" placeholder="Enter book genre" />
        </div>
        <div className='flex justify-center items-center gap-3'>
          <label htmlFor="quantity">Quantity:</label>
          <input className='border-1 border-slate-500 rounded-lg p-1' onChange={handleAvailable} type="number" value={available} id="quantity" placeholder="Enter quantity" />
        </div>
        <div className="btn w-full flex justify-center items-center"><button type='submit' className='bg-slate-300 rounded-lg p-2 hover:bg-slate-400 cursor-pointer'>UPDATE</button></div>
      </form>
    </div>
  )
}

export default Update