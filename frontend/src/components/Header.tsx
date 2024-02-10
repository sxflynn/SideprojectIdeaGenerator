import {Container, Text} from '@mantine/core';
import classes from './Header.module.css'


export function Header() {

    return (
        <header className={classes.header}>
           <Container size="md"> 
           <Text>Side Project Idea Generator</Text>
           </Container>
        </header>
        

    )
}