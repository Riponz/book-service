import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import Update from '../Components/Update'

function Details() {

    const { id } = useParams()
    const navigate = useNavigate()

    const GET_BOOK_URL = `http://127.0.0.1:8000/api/v1/books/${id}`

    const [book, setBook] = useState()
    const [update, setUpdate] = useState(false)

    useEffect(() => {
        const fetchBook = async () => {
            await axios.get(GET_BOOK_URL)
                .then(data => {
                    setBook(data?.data?.data)
                }).catch(err => {
                    console.log(err)
                })
        }

        fetchBook()
    }, [update])

    const handleUpdatePopUp = () => {
        setUpdate(!update)
    }


    return (
        <div className='h-[75%] w-full flex justify-center items-center'>

            {update && <Update id={book?.id} update={update} toggle={setUpdate} />}

            <div className="container bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[40%] h-[50%] flex flex-col justify-center items-center gap-4">
                <div className="details flex flex-col justify-center items-center gap-4">
                    <div className='text-4xl font-bold'>{book?.title}</div>
                    <div className="metadata text-sm"><span className='font-semibold text-slate-500'>By</span>: {book?.author} <span className='font-semibold text-slate-500'>Genre</span>: {book?.genre}</div>
                    <div className="metadata text-sm"><span className='font-semibold'>Available</span>: {book?.availability}</div>
                </div>
                <div onClick={handleUpdatePopUp} className="delete-btn cursor-pointer bg-green-400 p-2 rounded-xl hover:bg-green-500 hover:shadow-sm hover:shadow-slate-400">Update</div>
            </div>

        </div>
    )
}

export default Details