import React, { useState } from 'react';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

const App: React.FC = () => {
  const [input, setInput] = useState('Enter your prompt here ...');
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = () => {
    setIsLoading(true);
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInput(event.target.value);
  };

  return (
    <div className={`h-screen w-screen bg-yolomergebot bg-cover flex justify-center items-center ${inter.className}`}>
      {/* Centered container for the input */}
      <div className="relative flex justify-center items-center">
        {/* Image acting as the background for the input */}
        <img
          src="/images/app/text_box.jpeg" // Update with your image path
          alt="center"
          className="h-40 object-cover" // Adjust width and height as needed
        />
        {/* Transparent input box */}
        <input
          type="text"
          value={input}
          onChange={handleChange}
          className="absolute w-80 bg-transparent text-black text-center border-none outline-none placeholder-black"
          style={{ top: '50%', transform: 'translateY(-50%)' }} 
        />
      </div>
      {isLoading && <div className="absolute top-0 left-0 w-full h-full bg-white bg-opacity-50 flex justify-center items-center">Loading...</div>}
    </div>
  );
};

export default App;