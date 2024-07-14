import { RootState } from '@/redux/store';
import { useEffect } from 'react';
import { useSelector } from 'react-redux';

const ReduxFetchExample = () => {
  // access the redux state as such
  const { uid } = useSelector((state: RootState) => state.user);

  useEffect(() => {
    if (!uid) return;
    console.log('the uid of the user is ', uid);
  }, [uid]);

  return <div>ReduxFetchExample</div>;
};

export default ReduxFetchExample;
