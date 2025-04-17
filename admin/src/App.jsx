import './App.css'
import { Routes, Route } from 'react-router-dom'
import Navbar from './Components/Navbar'
import Inventory from './Pages/Inventory'
import AddBook from './Pages/AddBook'
import Users from './Pages/Users'
import { ToastContainer } from 'react-toastify'
import RentalsHistory from './Pages/RentalsHistory'
import bg from "./assets/bg.jpg"
import Details from './Pages/Details'
import Update from './Components/Update'

// style={{ backgroundImage: `url(${bg})` }}

function App() {

  return (
    <div className='w-full h-full overflow-x-hidden' >
      <ToastContainer />
      <Navbar />
      <Routes>
        <Route path="admin/" element={<Inventory />} />
        <Route path="admin/book/:id" element={<Details />} />
        <Route path="admin/add-book" element={<AddBook />} />
        <Route path="admin/users" element={<Users />} />
        <Route path="admin/history" element={<RentalsHistory />} />
        <Route path="admin/update" element={<Update />} />
      </Routes>
    </div>
  )
}

export default App
