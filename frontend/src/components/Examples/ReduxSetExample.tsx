import { setUserUid } from '@/redux/slices/userSlice';
import { useEffect } from 'react';
import { useDispatch } from 'react-redux';

const ReduxSetExample = () => {
  // create an instance of the dispatch function
  const dispatch = useDispatch();

  useEffect(() => {
    // dispatch the action as such
    dispatch(setUserUid('e2d6c15f-6eae-57ed-8122-a801d3d4fd5c'));
  }, []);

  return <div>ReduxSetExample</div>;
};

export default ReduxSetExample;
