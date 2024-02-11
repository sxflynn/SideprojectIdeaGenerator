import { Text, List, Paper, Title } from "@mantine/core";

export type ProjectResponse = {
    project_title: string;
    description: string;
    technical_requirements: string[];
    user_stories: string[];
  }

type ProjectDisplayProps = {
    data: ProjectResponse;
  }

  export function ProjectDisplay({ data }: ProjectDisplayProps) {
    return (
      <Paper>
        <Title order={2}>{data.project_title}</Title>
        <Text>{data.description}</Text>
        <Text>Technical Requirements</Text>
        <List>
          {data.technical_requirements.map((requirement, index) => (
            <List.Item key={index}>{requirement}</List.Item>
          ))}
        </List>
        <Text>User Stories</Text>
        <List>
          {data.user_stories.map((story, index) => (
            <List.Item key={index}>{story}</List.Item>
          ))}
        </List>
      </Paper>
    );
  }