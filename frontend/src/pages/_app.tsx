import { store } from '@/redux/store';
import '@/styles/globals.css';
import { AppPropsWithLayout } from '@/types/page';
import { QueryClient as ReactQueryClient, QueryClientProvider as ReactQueryProvider } from '@tanstack/react-query';
import { ThemeProvider } from 'next-themes';
import { Provider as ReduxProvider } from 'react-redux';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function App({ Component, pageProps }: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page) => page);
  const reactQueryClient = new ReactQueryClient();

  return (
    <ReactQueryProvider client={reactQueryClient}>
      <ReduxProvider store={store}>
        <ThemeProvider attribute="class">{getLayout(<Component {...pageProps} />)}</ThemeProvider>
        <ToastContainer />
      </ReduxProvider>
    </ReactQueryProvider>
  );
}
