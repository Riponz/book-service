import React, { useState } from 'react'
import axios from 'axios'
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';



function Register() {

    const [name, setName] = useState()
    const [username, setUSername] = useState()
    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const navigate = useNavigate()
    const notify = (msg) => toast(msg)

    const AUTH_URL = "https://user-service-koxz.onrender.com"

    const handleRegister = async (e) => {
        e.preventDefault()
        await axios.post(`${AUTH_URL}/register`, {
            name,
            username,
            email,
            password
        }).then(async (data) => {
            console.log(data.status)
            Cookies.set('token', data?.data?.access_token, { expires: 1 });
            notify("Registered Successfully")
            navigate("/")

        }).catch(err => {
            console.log(err?.response)
            notify(err?.response.data.error)
        })
    }

    const handleName = (e) => {
        setName(e.target.value)
    }

    const handleUsername = (e) => {
        setUSername(e.target.value)
    }

    const handleEmail = (e) => {
        setEmail(e.target.value)
    }

    const handlePassword = (e) => {
        setPassword(e.target.value)
    }

    const handleLogin = () => {
        navigate("/login")
    }




    return (
        <div className='w-full h-full flex justify-center items-center' >

            <div className="container bg-white/30 shadow-xl bg-clip-padding backdrop-filter  backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[22%] flex flex-col justify-center items-center gap-6 px-4 py-8 rounded-lg ">
                <div className='text-4xl font-bold'>register</div>
                <form onSubmit={handleRegister} className='flex flex-col justify-center w-[90%] items-center gap-6' action="">
                    <input onChange={handleName} className='border-1 w-full p-1 border-slate-500 rounded-sm outline-0' type="text" name='name' placeholder='name' value={name} />
                    <input onChange={handleUsername} className='border-1 w-full p-1 border-slate-500 rounded-sm outline-0' type="text" name='username' placeholder='username' value={username} />
                    <input onChange={handleEmail} className='border-1 w-full p-1 border-slate-500 rounded-sm outline-0' type="email" name='email' placeholder='email' value={email} />
                    <input onChange={handlePassword} className='border-1 w-full p-1 border-slate-500 rounded-sm outline-0' type="password" name='password' placeholder='password' value={password} />
                    <input className='border-1 border-slate-500 rounded-md px-3 py-1' type="submit" value="register" />
                </form>
                <div className='text-xs'>Already Registered? <span onClick={handleLogin} className='cursor-pointer font-semibold select-none'>Login</span></div>
            </div>

        </div>
    )
}

export default Register