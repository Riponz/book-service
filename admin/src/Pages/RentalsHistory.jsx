import axios from 'axios'
import React, { useEffect, useState } from 'react'

function RentalsHistory() {

    const [rentals, setRentals] = useState()
    const GET_RENTALS_URL = "https://user-service-koxz.onrender.com/api/v1/rents/"

    useEffect(() => {
        const fetchRentals = async () => {
            await axios.get(GET_RENTALS_URL)
                .then(data => {
                    setRentals(data?.data?.data)
                })
        }
        fetchRentals()
    }, [])


    return (
        <div className='w-full h-full flex justify-center items-start'>

            <table className="w-[85%] border border-gray-300 rounded-lg shadow-sm">
                <tr className="bg-gray-100">
                    <th className="px-4 py-2 text-left border-b">user_id</th>
                    <th className="px-4 py-2 text-left border-b">book_id</th>
                    <th className="px-4 py-2 text-left border-b">returned</th>
                </tr>
                {
                    rentals?.map(rent => (
                        <tr className="hover:bg-gray-50">
                            <td className="px-4 py-2 border-b">{rent.user_id}</td>
                            <td className="px-4 py-2 border-b">{rent.book_id}</td>
                            <td className="px-4 py-2 border-b">{rent.returned ? "✅" : "❌"}</td>
                        </tr>
                    ))
                }
            </table>
        </div>
    )
}

export default RentalsHistory