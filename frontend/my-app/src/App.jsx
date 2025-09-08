import { useState } from 'react'
import { BrowserRouter as Router, Routes , Route } from 'react-router-dom'
import './App.css'
import StoryLoader from './components/StoryLoader'
import StoryGenerator from './components/StoryGenerator'
function App() {
  return (
  <Router>
    <div className='app-container'>
      <header>
        <h1>Interactive Story Generator</h1>
      </header>
      <main>
        <Routes>
          <Route path={"/stories/:id"}element= {<StoryLoader/>} ></Route>
          <Route  path={"/"}element= {<StoryGenerator/>}></Route>
        </Routes>
      </main>
    </div>
  </Router>
  )
}

export default App
