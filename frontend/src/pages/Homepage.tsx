import { Text } from '@mantine/core'
import { useState } from 'react';
import { Form } from '../components/Form'
import { ProjectDisplay, ProjectResponse } from '../components/ProjectDisplay';

export function Homepage() {
    const [projectData, setProjectData] = useState<ProjectResponse | null>(null);
    
    return (
        <>
        <Text pb="lg">Use this tool to generate a full stack side project based on your skills and interests.</Text>
        <Form onFormSubmit={setProjectData} />
        {projectData && <ProjectDisplay data={projectData} />}
        </>
    )
}