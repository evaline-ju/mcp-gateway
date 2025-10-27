### Build stage
FROM golang:1.24.0-alpine AS build
ENV CGO_ENABLED=0
ENV GOOS=linux

WORKDIR /src
COPY . .
RUN go mod download
RUN go build -o /golang-ext-proc-filter-binary .

### Release stage

FROM registry.access.redhat.com/ubi9/ubi-minimal

COPY --from=build /golang-ext-proc-filter-binary /golang-ext-proc-filter-binary

ENTRYPOINT ["/golang-ext-proc-filter-binary"]
