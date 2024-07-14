import axios from 'axios';

export type TCreatePrRes = {
  message: string;
};

// axios post request to http://localhost:8000/create_pr
// body should contain the prompt key

export const createPr = async (prompt: string): Promise<TCreatePrRes> => {
  try {
    const res = await axios.post('http://localhost:8000/create_pr', {
      prompt: prompt,
    });
    return res.data;
  } catch (e) {
    console.log('error while creating pr', e);
    return { message: 'Error while creating the PR. Please try again later!' };
  }
};
