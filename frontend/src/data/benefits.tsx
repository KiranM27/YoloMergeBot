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
  desc: 'YoloMergeBot reduces the time spent on menial tasks, thereby allowing developers to focus on what really matters.',
  image: <CodeImage />,
  bullets: [
    {
      title: 'Automated Code Changes',
      desc: 'Automatically analyzes requirements and modifies the codebase, reducing manual effort.',
      icon: <IconWrapper icon={<FaceSmileIcon />} />,
    },
    {
      title: 'Faster Turnaround',
      desc: 'Ensures faster turnaround times for minor changes, speeding up the development process.',
      icon: <IconWrapper icon={<ChartBarSquareIcon />} />,
    },
    {
      title: 'Efficient Task Management',
      desc: 'Streamlines task management by automating repetitive tasks, leading to a more productive environment.',
      icon: <IconWrapper icon={<CursorArrowRaysIcon />} />,
    },
  ],
};

export const SecondaryBenefits: TBenefits = {
  title: 'Other Benefits',
  desc: 'YoloMergeBot also comes with other features that make it a great choice for your development workflow.',
  image: <MobileImage />,
  bullets: [
    {
      title: 'Seamless Integration',
      desc: 'Easily integrates with existing CI/CD pipelines and development tools.',
      icon: <IconWrapper icon={<DevicePhoneMobileIcon />} />,
    },
    {
      title: 'Customizable Prompts',
      desc: 'Supports customizable prompts for more tailored code changes.',
      icon: <IconWrapper icon={<AdjustmentsHorizontalIcon />} />,
    },
    {
      title: 'Enhanced Collaboration',
      desc: 'Facilitates better collaboration by raising PRs for review, ensuring code quality and teamwork.',
      icon: <IconWrapper icon={<SunIcon />} />,
    },
  ],
};