import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Card from '../Components/Card'

function Inventory() {

    const [books, setBooks] = useState()
    const [refresh, setRefresh] = useState(false)
    const GET_BOOK_URL = "https://book-service-7p3c.onrender.com/api/v1/books"

    useEffect(() => {
      const fetchBooks = async () => {
        await axios.get(GET_BOOK_URL)
        .then(data => {
            setBooks(data?.data?.data)
        }).catch(err => {
            notify(err?.response.data.error)
        })
      }
      fetchBooks()
    }, [refresh])
    
  return (
    <div className='w-full h-full flex flex-col justify-start items-center gap-3'>
            {
                books?.map(book => (
                    <Card key={book.id} id={book.id}
                        title={book.title}
                        author={book.author}
                        genre={book.genre}
                        ref={refresh}
                        toggle = {setRefresh} />
                ))
            }
        </div>
  )
}

export default Inventory