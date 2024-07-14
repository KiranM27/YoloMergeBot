import Container from '@/components/Container';
import { PRODUCT_DESCRIPTION, PRODUCT_NAME } from '@/constants/meta';
import Head from 'next/head';
import React from 'react';
import Navbar from '@/layouts/Navbar';
import Footer from '@/layouts/Footer';

type Props = {
  children: React.ReactNode;
  title?: string;
  description?: string;
};

const PrimaryLayout: React.FC<Props> = ({ children, title, description }) => {
  return (
    <>
      {/* page meta data */}
      <Head>
        <title>{title ?? PRODUCT_NAME}</title>
        <meta name="description" content={description ?? PRODUCT_DESCRIPTION} />
      </Head>
      {/* end of page meta data */}

      <Navbar />
      <Container>{children}</Container>
      <Footer />
    </>
  );
};

export default PrimaryLayout;
