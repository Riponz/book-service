import React from 'react'
import { Link } from 'react-router-dom';
import Cookies from "js-cookie"
import { useNavigate } from 'react-router-dom';

function Navbar() {

    const navigate = useNavigate()

    const handleLogout = () => {
        Cookies.remove('token')
        navigate('/login')
    }

    return (
        <div className='select-none w-full px-8 h-[15%] flex justify-between items-center bg-white/30 shadow-xl bg-clip-padding backdrop-filter  backdrop-blur backdrop-saturate-100 backdrop-contrast-100 mb-8'>
            <div className="logo text-xl font-bold"><Link to="/">Book Rental</Link></div>
            <div className="menu flex justify-evenly items-center gap-4">
                <Link to="/"><div className="item font-semibold">Books</div></Link>
                <Link to="/rentals"><div className="item font-semibold">Rentals</div></Link>
                <Link to="/account"><div className="item font-semibold">Profile</div></Link>
                <div onClick={handleLogout} className="logout inline-block rounded bg-red-500 text-neutral-50 shadow-[0_4px_9px_-4px_rgba(51,45,45,0.7)] hover:bg-red-600 hover:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] focus:bg-red-800 focus:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] active:bg-red-700 active:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal transition duration-150 ease-in-out focus:outline-none focus:ring-0">logout</div>
            </div>
        </div>
    )
}

export default Navbar