import Link from 'next/link';
import React from 'react';
import Container from '@/components/Container';
import { COPYRIGHT, PRODUCT_DESCRIPTION, PRODUCT_NAME } from '@/constants/meta';
import Twitter from '@/public/icons/socials/Twitter';
import Facebook from '@/public/icons/socials/Facebook';
import Instagram from '@/public/icons/socials/Instagram';
import LinkedIn from '@/public/icons/socials/LinkedIn';

export default function Footer() {
  // navigation items
  // at the moment, all pages are linked to the home page
  const navigation = [
    { name: 'Product', href: '/' },
    { name: 'Features', href: '/' },
    { name: 'Pricing', href: '/' },
    { name: 'Company', href: '/' },
    { name: 'Blog', href: '/' },
  ];

  // legal items
  // at the moment, all pages are linked to the home page
  const legal = [
    { name: 'Terms', href: '/' },
    { name: 'Privacy', href: '/' },
    { name: 'Legal', href: '/' },
  ];

  // social items
  const socials = [
    {
      name: 'Twitter',
      href: 'https://twitter.com',
      element: <Twitter />,
    },
    {
      name: 'Facebook',
      href: 'https://facebook.com',
      element: <Facebook />,
    },
    {
      name: 'Instagram',
      href: 'https://instagram.com',
      element: <Instagram />,
    },
    {
      name: 'LinkedIn',
      href: 'https://linkedin.com',
      element: <LinkedIn />,
    },
  ];

  return (
    <div className="relative p-8">
      <Container>
        <div className="grid grid-cols-1 gap-10 pt-10 mx-auto mt-5 border-t border-gray-100 dark:border-trueGray-700 lg:grid-cols-5">
          <div className="lg:col-span-2">
            {/* product name and desc */}
            <div>
              <Link href="/" className="flex items-center space-x-2 text-2xl font-medium text-indigo-500 dark:text-gray-100">
                <span>{PRODUCT_NAME}</span>
              </Link>
            </div>

            <div className="max-w-md mt-4 text-gray-500 dark:text-gray-400">{PRODUCT_DESCRIPTION}</div>

            <div className="max-w-md mt-4 text-gray-500 dark:text-gray-400">Note: An asterisk (*) denotes placeholder data.</div>
          </div>
          {/* product name and desc end */}

          {/* links to other pages */}
          <div className="col-span-1">
            <div className="flex flex-wrap w-full -mt-2 -ml-3 lg:ml-0">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="w-full px-4 py-2 text-gray-500 rounded-md dark:text-gray-300 hover:text-indigo-500 focus:text-indigo-500 focus:bg-indigo-100 focus:outline-none dark:focus:bg-trueGray-700"
                >
                  {item.name}
                </Link>
              ))}
            </div>
          </div>
          {/* links to other pages end */}

          {/* legal links */}
          <div className="col-span-1">
            <div className="flex flex-wrap w-full -mt-2 -ml-3 lg:ml-0">
              {legal.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="w-full px-4 py-2 text-gray-500 rounded-md dark:text-gray-300 hover:text-indigo-500 focus:text-indigo-500 focus:bg-indigo-100 focus:outline-none dark:focus:bg-trueGray-700"
                >
                  {item.name}
                </Link>
              ))}
            </div>
          </div>
          {/* legal links */}

          {/* social links */}
          <div className="col-span-1">
            <div>Follow us</div>
            <div className="flex mt-5 space-x-5 text-gray-400 dark:text-gray-500">
              {socials.map((item) => {
                return (
                  <a href={item.href} target="_blank" rel="noopener" key={item.name}>
                    <span className="sr-only">{item.name}</span>
                    {item.element}
                  </a>
                );
              })}
            </div>
          </div>
        </div>
        {/* social links end */}

        {/* copyright */}
        <div className="mt-10 text-sm text-center text-gray-600 dark:text-gray-400">{COPYRIGHT}</div>
      </Container>
    </div>
  );
}
