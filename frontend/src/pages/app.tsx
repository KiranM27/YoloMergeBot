import React, { useState } from 'react';
import { Inter } from 'next/font/google';
import { ArrowRightCircleIcon } from '@heroicons/react/24/solid';
import IconWrapper from '@/components/IconWrapper';

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
      {/* Holding Container for the Input Box and the Send Button */}
      <div className="flex flex-row gap-4 justify-center items-center">
        <div className="relative">
          {/* Image acting as the background for the input */}
          <img src="/images/app/text_box.jpeg" alt="center" className="h-40 object-cover" />

          <div className="h-full w-full absolute top-0 left-0 flex justify-center items-center px-8">
            <input type="text" value={input} onChange={handleChange} className="w-full bg-transparent text-black text-center border-none outline-none placeholder-black " />
          </div>
          {/* Transparent input box */}
        </div>
        <ArrowRightCircleIcon className="h-24 w-24" />
      </div>

      {isLoading && <div className="absolute top-0 left-0 w-full h-full bg-white bg-opacity-50 flex justify-center items-center">Loading...</div>}
    </div>
  );
};

export default App;
