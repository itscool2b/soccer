import React from 'react';
import WPS_Logo from '../public/WPS_Logo.png'

function Header() {
    return (
      <header className="bg-blue-500 text-white p-3 shadow-md flex flex-row items-center justify-between fixed top-0 left-0 right-0">
        <img
          className="w-1/5 md:w-1/8 lg:w-1/12 xl:w-1/12"
          src={WPS_Logo}
          alt="Logo"
          style={{ maxWidth: '15vw', height: 'auto', borderRadius: '10px', marginRight: '2vw' }}
        />
        <h1 className="text-2xl font-bold">Soccer App</h1>
        <button className="bg-blue-700 hover:bg-blue-800 text-white font-semibold mr-7 py-2 px-4 border border-blue-700 rounded shadow" method="POST">
            Add Game
        </button>
      </header>
    );
  }
  

export default Header;
