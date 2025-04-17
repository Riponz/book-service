import React, { useEffect, useState } from 'react'
import Cookies from 'js-cookie'
import axios from 'axios'
import { toast } from 'react-toastify';
import { useUser } from '../Components/Context'
import { jwtDecode } from 'jwt-decode'

function Account() {

    const { user, setUser } = useUser()
    const token = Cookies.get('token')
    const notify = (msg) => toast(msg);
    const GET_USER_API = "https://user-service-koxz.onrender.com/users/me/"

    useEffect(() => {
        const isTokenValid = (token) => {
            try {
                const decoded = jwtDecode(token);
                const now = Date.now() / 1000; // in seconds
                return decoded.exp > now;
            } catch (e) {
                return false;
            }
        }

        const loggedIn = token && isTokenValid(token)

        if (!loggedIn) {
            notify("Token Expired. Login Again")
            navigate('/login')
        }
    }, [])



    return (
        <div className='h-[75%] w-full flex justify-center items-center'>
            <div key={user?.id} className="container bg-white/30 shadow-xl bg-clip-padding backdrop-filter rounded-xl backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[40%] h-[50%] flex flex-col justify-center items-center gap-4">
                <div className="details flex flex-col justify-center items-center gap-2">
                    <div className='text-2xl font-bold'>{user?.name}</div>
                    <div className="metadata text-sm"><span className='font-semibold'>username</span>: {user?.username}</div>
                    <div className="metadata text-sm"><span className='font-semibold'>Email</span>: {user?.email}</div>
                </div>
            </div>
        </div>
    )
}

export default Account