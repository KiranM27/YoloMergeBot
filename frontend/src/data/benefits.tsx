import { FaceSmileIcon, ChartBarSquareIcon, CursorArrowRaysIcon, DevicePhoneMobileIcon, AdjustmentsHorizontalIcon, SunIcon } from '@heroicons/react/24/solid';
import IconWrapper from '@/components/IconWrapper';
import CodeImage from '@/public/icons/landing/CodeImage';
import MobileImage from '@/public/icons/landing/MobileImage';

// create a type for the data
export type TBenefits = {
  title: string;
  desc: string;
  image: React.ReactNode;
  bullets: TBullet[];
};

export type TBenefitBulletIcon = React.ReactNode;

export type TBullet = {
  title: string;
  desc: string;
  icon: TBenefitBulletIcon;
};

export const IconWrapperClass = 'w-7 h-7 text-white';

export const PrimaryBenefits: TBenefits = {
  title: 'Benefits',
  desc: 'HyperNext comes fully equipped with utilites such as Redux, React Query, React Portals and more to help you hit the ground running.',
  image: <CodeImage />,
  bullets: [
    {
      title: 'Redux',
      desc: 'Redux is a predictable state container for JavaScript apps.',
      icon: <IconWrapper icon={<FaceSmileIcon />} />,
    },
    {
      title: 'React Query',
      desc: 'React Query is a powerful data fetching library for React.',
      icon: <IconWrapper icon={<ChartBarSquareIcon />} />,
    },
    {
      title: 'React Portals',
      desc: 'Render components outside their parent hierarchy with Portals.',
      icon: <IconWrapper icon={<CursorArrowRaysIcon />} />,
    },
  ],
};

export const SecondaryBenefits: TBenefits = {
  title: 'Other Benefits',
  desc: 'HyperNext also comes with other features that make it a great choice for your next project.',
  image: <MobileImage />,
  bullets: [
    {
      title: 'Mobile Responsive Template',
      desc: 'HyperNext is designed as a mobile first responsive template.',
      icon: <IconWrapper icon={<DevicePhoneMobileIcon />} />,
    },
    {
      title: 'Powered by Next.js & TailwindCSS',
      desc: 'This template is powered by latest technologies and tools.',
      icon: <IconWrapper icon={<AdjustmentsHorizontalIcon />} />,
    },
    {
      title: 'Dark & Light Mode',
      desc: 'HyperNext comes with a zero-config light & dark mode. ',
      icon: <IconWrapper icon={<SunIcon />} />,
    },
  ],
};
