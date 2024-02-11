import { Box, Button, MultiSelect } from "@mantine/core";
import { useForm } from "@mantine/form";
import { ProjectResponse } from "./ProjectDisplay";

type TechList = {
  unknown_tech: string[];
  known_tech: string[];
  topics: string[];
}

type FormProps = {
  onFormSubmit: (data: ProjectResponse) => void;
}


export function Form({ onFormSubmit }: FormProps) {
    
  const form = useForm<TechList>({
    initialValues: {
      unknown_tech: [],
      known_tech: [],
      topics: [],
    },
  });

  const handleSubmit = async (values: TechList) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/prompt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ProjectResponse = await response.json();
      onFormSubmit(data);
    } catch (error) {
      console.error('Error:', error);
    }
  }
  


  return (
    <Box>
      <form onSubmit={form.onSubmit(handleSubmit)}>
        {/* <TextInput label="Tech you know" {...form.getInputProps("knownTech")} /> */}
        <MultiSelect
      label="Tech you know"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      searchable
      {...form.getInputProps("known_tech")}
    />
        <MultiSelect
      label="Tech you don't know"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      searchable
      {...form.getInputProps("unknown_tech")}
    />
        <MultiSelect
      label="Topics you like"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      searchable
      {...form.getInputProps("topics")}
    />
      <Button type="submit">Submit</Button>
      
  

      </form>
    </Box>
  );
}
