import React from 'react';
import { TBenefitBulletIcon } from '@/data/benefits';

type Props = {
  icon: TBenefitBulletIcon;
  title: string;
  children: React.ReactNode;
};

const BenefitBullet = ({ icon, title, children }: Props) => {
  return (
    <>
      <div className="flex items-start mt-8 space-x-3">
        <div className="flex items-center justify-center flex-shrink-0 mt-1 bg-indigo-500 border-none rounded-md w-11 h-11">{icon}</div>
        <div>
          <h4 className="text-xl font-medium text-gray-800 dark:text-gray-200">{title}</h4>
          <p className="mt-1 text-gray-500 dark:text-gray-400">{children}</p>
        </div>
      </div>
    </>
  );
};

export default BenefitBullet;
