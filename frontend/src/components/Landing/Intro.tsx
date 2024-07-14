import Container from '@/components/Container';
import { PRODUCT_DESCRIPTION } from '@/constants/meta';
import LaunchImage from '@/public/icons/landing/LaunchImage';
import AmazonLogo from '@/public/icons/logos/AmazonLogo';
import GithubIcon from '@/public/icons/logos/GithubIcon';
import MicrosoftLogo from '@/public/icons/logos/MicrosoftLogo';
import NetflixLogo from '@/public/icons/logos/NetflixLogo';
import SonyLogo from '@/public/icons/logos/SonyLogo';
import VerizonLogo from '@/public/icons/logos/VerizonLogo';

const Intro = () => {
  const socialProofs = [
    {
      name: 'Amazon',
      element: <AmazonLogo />,
    },
    {
      name: 'Miccrosft',
      element: <MicrosoftLogo />,
    },
    {
      name: 'Netflix',
      element: <NetflixLogo />,
    },
    {
      name: 'Sony',
      element: <SonyLogo />,
    },
    {
      name: 'Verizon',
      element: <VerizonLogo />,
    },
  ];

  return (
    <>
      <Container className="flex flex-wrap flex-row items-center md:my-10 lg:my-20 ">
        <div className="flex items-center w-full lg:w-1/2">
          <div className="max-w-2xl mb-8">
            <h1 className="text-4xl font-bold leading-snug tracking-tight text-gray-800 lg:text-4xl lg:leading-tight xl:text-6xl xl:leading-tight dark:text-white">
              Prompt to PR
            </h1>
            <p className="py-5 text-xl leading-normal text-gray-500 lg:text-xl xl:text-2xl dark:text-gray-300">{PRODUCT_DESCRIPTION}</p>

            <div className="flex flex-col items-start space-y-3 sm:space-x-4 sm:space-y-0 sm:items-center sm:flex-row">
              <a
                href="https://github.com/KiranM27/prompt-to-pr"
                target="_blank"
                rel="noopener"
                className="px-8 py-4 text-lg font-medium text-center text-white bg-indigo-600 rounded-md flex flex-row justify-center items-center space-x-4"
              >
                <GithubIcon />
                <span> View on Github</span>
              </a>
            </div>
          </div>
        </div>
        <div className="flex items-center justify-center w-full lg:w-1/2">
          <div>
            <LaunchImage />
          </div>
        </div>
      </Container>

      {/* social proof */}
      <Container>
        <div className="flex flex-col justify-center">
          <div className="text-xl text-center text-gray-700 dark:text-white">
            Trusted by <span className="text-indigo-600">2000+</span> customers worldwide. Not the ones below.
          </div>

          {/* company logos */}
          <div className="flex flex-wrap justify-center gap-5 mt-10 md:justify-around">
            {socialProofs.map((proof) => {
              return (
                <div className="pt-2 text-gray-400 dark:text-gray-400" key={proof.name}>
                  {proof.element}
                </div>
              );
            })}
          </div>
          {/* company logos end */}
        </div>
      </Container>
      {/* social proofs end */}
    </>
  );
};

export default Intro;
