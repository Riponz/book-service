import React from 'react'
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

function Navbar() {

    const navigate = useNavigate()

    return (
        <div className='select-none w-full px-8 h-[15%] flex justify-between items-center bg-white/30 shadow-xl bg-clip-padding backdrop-filter  backdrop-blur backdrop-saturate-100 backdrop-contrast-100 mb-8'>
            <div className="logo text-xl font-bold"><Link to="/">Book Rental<sup className='text-xs font-medium'>admin</sup></Link></div>
            <div className="menu flex justify-evenly items-center gap-4">
                <Link to="/"><div className="item font-semibold">Inventory</div></Link>
                <Link to="/add-book"><div className="item font-semibold">Add</div></Link>
                <Link to="/users"><div className="item font-semibold">Users</div></Link>
                <Link to="/history"><div className="item font-semibold">Rentals</div></Link>
            </div>
        </div>
    )
}

export default Navbar