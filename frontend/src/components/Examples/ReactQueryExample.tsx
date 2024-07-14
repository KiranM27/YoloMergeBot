import React from 'react';
import { useGithubUser } from '@/api/github.api';

const ReactQueryExample = () => {
  const { isLoading, error, data } = useGithubUser();

  if (isLoading) return 'Loading...';
  if (error) console.log('An error occurred while fetching the user data ', error);

  return (
    <div>
      <h1>{data?.name}</h1>
      <p>{data?.bio}</p>
    </div>
  );
};

export default ReactQueryExample;
