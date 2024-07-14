import { PayloadAction, createSlice } from '@reduxjs/toolkit';
import { IUser } from '../redux.types';

const initialState: IUser = {
  uid: '',
  email: '',
};

export const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser: (state, action: PayloadAction<IUser>) => {
      state.uid = action.payload.uid;
      state.email = action.payload.email;
    },
    setUserEmail: (state, action: PayloadAction<string>) => {
      state.email = action.payload;
    },
    setUserUid: (state, action: PayloadAction<string>) => {
      state.uid = action.payload;
    },

    clearUser: (state) => {
      state.uid = '';
      state.email = '';
    },
  },
});

export const { setUser, setUserEmail, setUserUid, clearUser } = userSlice.actions;

export default userSlice.reducer;
