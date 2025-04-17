import React, { useEffect, useState } from 'react'
import axios from 'axios'
import UserCard from '../Components/UserCard'

function Users() {

  const [users, setUsers] = useState()
  const GET_USERS_URL = "http://127.0.0.1:5000/api/v1/users/"

  useEffect(() => {
    const fetchUsers = async () => {
      await axios.get(GET_USERS_URL)
      .then(data => {
        setUsers(data?.data?.data)
      }).catch(err => {
        console.log(err)
      })
    }
    fetchUsers()
  }, [])
  
  return (
    <div className='w-full h-full flex flex-col justify-start items-center gap-3'>
            {
                users?.map(user => (
                    <UserCard key={user.id} id={user.id}
                        name={user.name}
                        username={user.username}
                        email={user.email} />
                ))
            }
        </div>
  )
}

export default Users