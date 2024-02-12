import { useState } from 'react';
import { Form } from '../components/Form'
import { ProjectDisplay, ProjectResponse } from '../components/ProjectDisplay';

export function Homepage() {
    const [projectData, setProjectData] = useState<ProjectResponse | null>(null);
    
    return (
        <>
        <Form onFormSubmit={setProjectData} />
        {projectData && <ProjectDisplay data={projectData} />}
        </>
    )
}