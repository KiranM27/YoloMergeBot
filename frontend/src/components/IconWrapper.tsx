import { ReactElement, cloneElement } from 'react';
import { IconWrapperClass } from '@/data/benefits';

interface IconWrapperProps {
  icon: ReactElement;
}

const IconWrapper: React.FC<IconWrapperProps> = ({ icon }) => {
  const clonedIcon = cloneElement(icon, {
    className: IconWrapperClass,
  });

  return <>{clonedIcon}</>;
};

export default IconWrapper;
