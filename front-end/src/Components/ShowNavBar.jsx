import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'

function ShowNavBar({ children }) {

    const [showNav, setShowNav] = useState(false)

    const location = useLocation()

    useEffect(() => {
        if (location.pathname === "/login" || location.pathname === "/register") {
            setShowNav(false)
        } else {
            setShowNav(true)
        }
    }, [location])


    return (
        <>{showNav && children}</>
    )
}

export default ShowNavBar
