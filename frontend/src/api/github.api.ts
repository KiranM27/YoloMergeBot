// api/github.api.ts
import { useQuery } from '@tanstack/react-query';

export type TGithubUser = {
  name: string;
  bio: string;
};

export const fetchGithubUser = async () => {
  const res = await fetch('https://api.github.com/users/kiranm27');
  if (!res.ok) {
    throw new Error('Network response was not ok');
  }
  const data = await res.json();
  const user: TGithubUser = {
    name: data?.name || '',
    bio: data?.bio || '',
  };
  return user;
};

export const useGithubUser = () => {
  return useQuery(['githubUser'], fetchGithubUser);
};
