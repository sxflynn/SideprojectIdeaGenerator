import { useState } from "react";
import { Box, Button, Group, MultiSelect, Switch } from "@mantine/core";
import { useForm } from "@mantine/form";
import { ProjectResponse } from "./ProjectDisplay";
import {
  database_management_systems,
  javascript_frameworks,
  programming_languages,
  server_side_frameworks,
} from "./techlist";
import { Error } from "./Error";
import { Loading } from "./Loading";

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
  "Database management system",
);

const jsFrameworkOptions = prepareData(
  javascript_frameworks,
  "JavaScript framework",
);

const serverSideFrameworkOptions = prepareData(
  server_side_frameworks,
  "Server-side framework",
);

const programmingLanguageOptions = prepareData(
  programming_languages,
  "programming language",
);

const allOptions = [
  ...databaseOptions,
  ...programmingLanguageOptions,
  ...jsFrameworkOptions,
  ...serverSideFrameworkOptions,
];

type FormProps = {
  onFormSubmit: (data: ProjectResponse) => void;
};

export function Form({ onFormSubmit }: FormProps) {
  const [streaming, setStreaming] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<null | string>(null);
  const [streamingResponses, setStreamingResponses] = useState<ProjectResponse[]>([]);


  const form = useForm<TechList>({
    initialValues: {
      unknown_tech: [],
      known_tech: [],
      topics: [],
    },
    validate: {
      known_tech: (value) =>
        value.length === 0 ? "Please select at least one technology." : null,
      topics: (value) =>
        value.length === 0
          ? "Please select at least one topic of interest."
          : null,
    },
  });

  const formatTechSelections = (selectedTech: string[], options: SelectOption[]): string[] => {
    return selectedTech.map((selectedValue) => {
      const option = options.find((option) => option.value === selectedValue);
      return `${selectedValue} ${option?.category}`;
    });
  };


  const handleSubmit = async (values: TechList) => {
    if (streaming){
      handleStreamingSubmit(values);
    } else {
      handleRegularSubmit(values);
    }
  }

  const handleStreamingSubmit = (values: TechList) => {
    console.log("Streaming mode enabled!")
    setLoading(true);
    setError(null);
    setStreamingResponses([]);

    const formattedKnownTech = formatTechSelections(values.known_tech, allOptions);
    const formattedUnknownTech = formatTechSelections(values.unknown_tech, allOptions);

    const payload = {
      known_tech: formattedKnownTech,
      unknown_tech: formattedUnknownTech,
      topics: values.topics,
    };

    const ws = new WebSocket(`ws://${import.meta.env.VITE_LLM_BASE_URL}/promptstreaming`);
    ws.onopen = () => {
      ws.send(JSON.stringify(payload));
    };

    ws.onmessage = (event) => {
      const newResponse:ProjectResponse = JSON.parse(event.data);
      setStreamingResponses((prevResponses) => [...prevResponses, newResponse]);
    }

    ws.onerror = (event) => {
      setError("WebSocket error, check the console for more details");
      console.error(event)
    }

    ws.onclose = () => {
      setLoading(false);
      if (streamingResponses.length > 0) {
        onFormSubmit(streamingResponses[streamingResponses.length - 1]);
      }
    }

  }

  const handleRegularSubmit = async (values: TechList) => {
    setLoading(true);
    const formattedKnownTech = formatTechSelections(values.known_tech, allOptions);
    const formattedUnknownTech = formatTechSelections(values.unknown_tech, allOptions);


    const payload = {
      known_tech: formattedKnownTech,
      unknown_tech: formattedUnknownTech,
      topics: values.topics,
    };

    try {
      console.log(values);
      setError(null);
      const response = await fetch(
        `http://${import.meta.env.VITE_LLM_BASE_URL}/prompt`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        },
      );

      if (response.status === 200) {
        const data: ProjectResponse = await response.json();
        onFormSubmit(data);
      } else if (response.status === 429) {
        setError(
          "You've exceeded the rate limit. Please try again in a few minutes.",
        );
      } else {
        setError("There was an error connecting to the AI server.");
      }
    } catch (error) {
      console.error("Error:", error);
      setError("Network error. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
  <>
    <Switch
      size="md"
        label="Streaming mode"
        checked={streaming}
        onChange={(event) => setStreaming(event.currentTarget.checked)}
        />
    <Box>
      <form onSubmit={form.onSubmit(handleSubmit)}>
        {/* <TextInput label="Tech you know" {...form.getInputProps("knownTech")} /> */}
        <MultiSelect
          pb="xl"
          label="Tech you know"
          data={allOptions}
          searchable
          {...form.getInputProps("known_tech")}
        />
        <MultiSelect
          pb="xl"
          label="Tech you don't know"
          data={allOptions}
          searchable
          {...form.getInputProps("unknown_tech")}
        />
        <MultiSelect
          pb="xl"
          label="Topics you like"
          data={["Swimming", "Dancing", "Basketball", "Reading"]}
          searchable
          {...form.getInputProps("topics")}
        />
        <Group>
          <Button type="submit" disabled={loading}>
            Submit
          </Button>
          {loading && <Loading />}
        </Group>
        {error && <Error error={error} onDismiss={() => setError(null)} />}
      </form>
    </Box>
    </>
  );
}
