import "@mantine/core/styles.css";
import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";
import { Homepage } from "./pages/Homepage";
import { Header } from "./components/Header"

export default function App() {
  return <MantineProvider theme={theme}>
    <Header/>
    <Homepage/>
    </MantineProvider>;
}
