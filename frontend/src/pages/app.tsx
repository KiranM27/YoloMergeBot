import { createPr } from '@/api/create_pr.api';
import { ArrowRightCircleIcon } from '@heroicons/react/24/solid';
import { Inter } from 'next/font/google';
import React, { useState } from 'react';
import { toast } from 'react-toastify';

const inter = Inter({ subsets: ['latin'] });

const App: React.FC = () => {
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    if (isLoading) return;
    setIsLoading(true);

    const res = await createPr(input);
    toast.info(res.message);
    setIsLoading(false);
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
            <input
              type="text"
              value={input}
              onChange={handleChange}
              className="w-full bg-transparent text-black text-center border-none outline-none placeholder-black "
              placeholder="Enter your prompt here ..."
            />
          </div>
          {/* Transparent input box */}
        </div>

        <div className="cursor-pointer" onClick={handleClick}>
          <ArrowRightCircleIcon className="h-24 w-24" />
        </div>
      </div>
    </div>
  );
};

export default App;
