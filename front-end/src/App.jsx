import './App.css'
import Login from './Pages/Login'
import Register from './Pages/Register'
import { Routes, Route } from "react-router-dom"
import Home from './Pages/Home'
import Navbar from './Components/Navbar'
import bg from "./assets/background.jpg"
import Account from './Pages/Account'
import Books from './Pages/Books'
import ShowNavBar from './Components/ShowNavBar'
import Detail from './Pages/Detail'
import { ToastContainer } from 'react-toastify'
import { UserProvider } from './Components/Context'

function App() {

  return (
    <div className='w-full h-full bg-cover overflow-x-hidden' style={{ backgroundImage: `url(${bg})` }}>
      <UserProvider>
        <ToastContainer />
        <ShowNavBar>
          <Navbar />
        </ShowNavBar>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/book/:id" element={<Detail />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/rentals" element={<Books />} />
          <Route path="/account" element={<Account />} />
        </Routes>
      </UserProvider>
    </div>
  )
}

export default App
