import {Container, Text, Title} from '@mantine/core';
import classes from './Header.module.css'


export function Header() {

    return (
        <header className={classes.header}>
           <Container size="md"> 
           <Title>Side Project Idea Generator</Title>
           </Container>
        </header>
        

    )
}