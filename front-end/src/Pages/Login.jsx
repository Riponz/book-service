import React, { useState } from 'react'
import axios from 'axios'
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';

function Login() {

    const [username, setUSername] = useState()
    const [password, setPassword] = useState()
    const navigate = useNavigate()

    const notify = (msg) => toast(msg)

    const AUTH_URL = "http://127.0.0.1:5000"

    const handleLogin = async (e) => {
        e.preventDefault()
        const formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);
        await axios.post(`${AUTH_URL}/token`, formData)
            .then(data => {
                console.log(data.status)
                Cookies.set('token', data?.data?.access_token, { expires: 1 });
                if (data.status === 200) {
                    notify("Login Successful")
                    navigate('/')
                }
                if (err?.response.status_code === 401) {
                    notify(err?.response.data.error)
                }

            })
            .catch(err => {
                notify(err?.response.data.error)

            })

    }

    const handleUsername = (e) => {
        setUSername(e.target.value)
    }

    const handlePassword = (e) => {
        setPassword(e.target.value)
    }

    const handleRegister = () => {
        navigate('/register')
    }

    return (
        <div className='w-full h-full flex justify-center items-center' >

            <div className="container bg-white/30 shadow-xl bg-clip-padding backdrop-filter  backdrop-blur backdrop-saturate-100 backdrop-contrast-100 w-[22%] flex flex-col justify-center items-center gap-6 px-4 py-8 rounded-lg ">
                <div className='text-4xl font-bold'>login</div>
                <form onSubmit={handleLogin} className='flex flex-col justify-center w-[90%] items-center gap-6' action="">

                    <input onChange={handleUsername} className='border-1 w-full p-1 border-slate-500 rounded-sm outline-0' type="text" name='username' placeholder='username' value={username} />
                    <input onChange={handlePassword} className='border-1 w-full p-1 border-slate-500 rounded-sm outline-0' type="password" name='password' placeholder='password' value={password} />
                    <input className='border-1 border-slate-500 rounded-md px-3 py-1' type="submit" value="login" />
                </form>
                <div className='text-xs'>New Here? <span onClick={handleRegister} className='cursor-pointer font-semibold select-none'>Register</span></div>
            </div>

        </div>
    )
}

export default Login