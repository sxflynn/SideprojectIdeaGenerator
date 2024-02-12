import { useState } from 'react';
import { Box, Button, Group, MultiSelect } from "@mantine/core";
import { useForm } from "@mantine/form";
import { ProjectResponse } from "./ProjectDisplay";
import {
  database_management_systems,
  javascript_frameworks,
  programming_languages,
  server_side_frameworks,
} from "./techlist";
import { Error } from './Error'
import { Loading } from './Loading';


type TechList = {
  unknown_tech: string[];
  known_tech: string[];
  topics: string[];
};

type SelectOption = {
  label: string;
  value: string;
  category: string;
};

const prepareData = (items: string[], categoryName: string): SelectOption[] =>
  items.map((item) => ({
    label: item,
    value: `${item} ${categoryName}`,
    category: categoryName,
  }));

const databaseOptions = prepareData(
  database_management_systems,
  "Database management system"
);

const jsFrameworkOptions = prepareData(
  javascript_frameworks,
  "JavaScript framework"
);

const serverSideFrameworkOptions = prepareData(
  server_side_frameworks,
  "Server-side framework"
);

const programmingLanguageOptions = prepareData(
  programming_languages,
  "programming language"
);

const allOptions = [...databaseOptions, ...programmingLanguageOptions, ...jsFrameworkOptions, ...serverSideFrameworkOptions];

type FormProps = {
  onFormSubmit: (data: ProjectResponse) => void;
};

export function Form({ onFormSubmit }: FormProps) {
  const [loading, setLoading] = useState(false);

  const [error, setError] = useState<null | string>(null);

  const form = useForm<TechList>({
    initialValues: {
      unknown_tech: [],
      known_tech: [],
      topics: [],
    },
    validate: {
      known_tech: (value) => (value.length === 0 ? 'Please select at least one technology.' : null),
      topics: (value) => (value.length === 0 ? 'Please select at least one topic of interest.' : null),
    }
  });

  const handleSubmit = async (values: TechList) => {
    setLoading(true);
    const formattedKnownTech = values.known_tech.map(selectedValue => {
      const option = allOptions.find(option => option.value === selectedValue);
      return `${selectedValue} ${option?.category}`;
    });

    const formattedUnknownTech = values.unknown_tech.map(selectedValue => {
      const option = allOptions.find(option => option.value === selectedValue);
      return `${selectedValue} ${option?.category}`;
    });

    const payload = {
      known_tech: formattedKnownTech,
      unknown_tech: formattedUnknownTech,
      topics: values.topics
    }
      
    try {
      console.log(values);
      const response = await fetch("http://localhost:8000/prompt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (response.status === 200){
        const data: ProjectResponse = await response.json();
        onFormSubmit(data);
      } else if (response.status === 429){
        setError("You've exceeded the rate limit. Please try again in a few minutes.")
      } else {
        setError('There was an error connecting to the AI server.')
      }


    } catch (error) {

      console.error("Error:", error);
      setError('Network error. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box>
      <form onSubmit={form.onSubmit(handleSubmit)}>
        {/* <TextInput label="Tech you know" {...form.getInputProps("knownTech")} /> */}
          <MultiSelect pb="xl"
            label="Tech you know"
            data={allOptions}
            searchable
            {...form.getInputProps("known_tech")}
          />
        <MultiSelect pb="xl"
          label="Tech you don't know"
          data={allOptions}
          searchable
          {...form.getInputProps("unknown_tech")}
        />
        <MultiSelect pb="xl"
          label="Topics you like"
          data={["Swimming", "Dancing", "Basketball", "Reading"]}
          searchable
          {...form.getInputProps("topics")}
        />
        <Group>
          <Button type="submit" disabled={loading}>Submit</Button>
          {loading && <Loading/>}
        </Group>
        {error && <Error error={error} onDismiss={() => setError(null)} />}
      </form>
    </Box>
  );
}
