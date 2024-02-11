import { useState } from 'react';
import {Text} from '@mantine/core';
import { Form } from '../components/Form'
import { ProjectDisplay, ProjectResponse } from '../components/ProjectDisplay';

export function Homepage() {
    const [projectData, setProjectData] = useState<ProjectResponse | null>(null);
    
    return (
        <>
        <Text>Use this form below</Text>
        <Form onFormSubmit={setProjectData} />
        {projectData && <ProjectDisplay data={projectData} />}
        </>
    )
}